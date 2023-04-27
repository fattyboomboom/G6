<template>
    <div class="Class-feed">
        <h1>Class Feed</h1>
        <div class="post-container">
            <v-card v-for="post in posts" :key="post.uid" class="post" variant="outlined">
                <v-card-title class="d-flex justify-space-between align-center ">
                    <div>
                        <v-avatar color="grey-darken-3"
                            image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"></v-avatar>
                        <span class="ml-5">{{ `${post.FirstName} ${post.LastName}` }}</span>
                    </div>

                    <v-menu offset-y>
                        <template v-slot:activator="{ props }">
                            <v-btn flat icon="mdi-dots-vertical" v-bind="props">
                            </v-btn>
                        </template>

                        <v-list>
                            <v-list-item v-if="currentUID === post.uid || currentUID === moderatorUID" @click="deletePost(post)">
                                <div class="d-flex align-center" style="color:rgb(180, 25, 25)">
                                    <v-list-item-title>Delete</v-list-item-title>
                                    <v-icon class="ml-2">mdi-delete</v-icon>
                                </div>
                            </v-list-item>
                            <v-list-item v-else @click="reportPost(post)">
                                <div class="d-flex align-center">
                                    <v-list-item-title>Report</v-list-item-title>
                                    <v-icon class="ml-2">mdi-flag</v-icon>
                                </div>
                            </v-list-item>
                        </v-list>
                    </v-menu>

                </v-card-title>
                <v-card-text class="text-h6">
                    {{ post.content }}
                </v-card-text>
                <v-card-actions>
                    <v-list-item class="w-100">


                        <template v-slot:append>
                            <div class="justify-self-end">
                                <span class="subtitle me-2">{{ formatDate(post.PostDate) }}</span>
                                <span class="me-2">·</span>
                                <span class="subtitle me-2">{{ formatTime(post.PostDate) }}</span>
                                <span class="me-1">·</span>
                                <v-btn class="me-1" @click="isLiked(post) ? unlikePost(post) : likePost(post)"
                                    :style="{ 'color': isLiked(post) ? '#C1121F' : 'black' }" icon>
                                    <v-icon v-if="!isLiked(post)">mdi-heart-outline</v-icon>
                                    <v-icon v-else>mdi-heart</v-icon>
                                </v-btn>
                                <span class="subheading ml-0">{{ post.likes.length }}</span>

                            </div>
                        </template>

                    </v-list-item>
                </v-card-actions>
            </v-card>
        </div>
    </div>
</template>
  
<script>
import { ref, onMounted } from "vue";
import { collection, query, where, onSnapshot, arrayUnion, arrayRemove, updateDoc, doc, getDocs} from "firebase/firestore";
import { db, auth } from "@/firebase";
import { onAuthStateChanged } from "firebase/auth"
import { useRoute } from "vue-router";

export default {
    name: "ClassFeed",
    setup() {
        const route = useRoute();
        const classPrefix = (route.params.classPrefix);
        const classNumber = (route.params.classNumber);
        const posts = ref([]);
        const error = ref("");
        const currentUID = ref(null);
        const moderatorUID = ref(null);

        const fetchPosts = async () => {
            try {
                const postRef = collection(db, "posts");
                const q = query(postRef,
                    where("classPrefix", "==", classPrefix),
                    where("classNumber", "==", classNumber),
                    where("postType", "==", "post"),
                    where("isDeleted", "==", false)
                );
                onSnapshot(q, (docSnap) => {
                    posts.value = docSnap.docs.map((doc) => {
                        const data = doc.data();
                        data.id = doc.id;
                        return data;
                    });
                    posts.value.sort((a, b) => b.PostDate - a.PostDate);
                    console.log(posts);
                });
            } catch (err) {
                error.value = err.message;
            }
        };

        const fetchClassData = async (classPrefix, classNumber) => {
            const querySnapshot = await getDocs(
                query(
                    collection(db, 'classes'),
                    where("prefix", "==", classPrefix),
                    where("classNum", "==", classNumber),
                    where("isDeleted", "==", false)
                )
            );
            if (querySnapshot.docs.length > 0) {
                return querySnapshot.docs[0].data();
            } else {
                throw new Error(`Class ${classPrefix} - ${classNumber} not found`);
            }
        };


        const getClassData = async () => {
            const classData = await fetchClassData(classPrefix, classNumber);
            moderatorUID.value = classData.moderatorUID;
        };



        onMounted(() => {
            fetchPosts();
        });
        onAuthStateChanged(auth, (user) => {
            if (user) {
                currentUID.value = auth.currentUser.uid;
            } else {
                currentUID.value = null;
            }
        });

        getClassData();
        return { posts, error, currentUID, moderatorUID };
    },
    methods: {
        formatTime(timestamp) {
            if (!timestamp) {
                return '';
            }
            const date = timestamp.toDate();
            const hours = date.getHours();
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const ampm = hours >= 12 ? 'PM' : 'AM';
            const twelveHours = hours % 12 || 12;
            return `${twelveHours}:${minutes} ${ampm}`;
        },

        formatDate(timestamp) {
            if (!timestamp) {
                return '';
            }
            const date = timestamp.toDate();
            const options = { month: 'numeric', day: 'numeric', year: '2-digit' };
            return new Intl.DateTimeFormat('en-US', options).format(date);
        },

        isLiked(post) {
            return post.likes.includes(auth.currentUser.uid);
        },
        async likePost(post) {
            try {
                const uid = auth.currentUser.uid;

                const postRef = doc(db, "posts", post.id);

                // Like the post by adding the user's UID to the likes array
                await updateDoc(postRef, {
                    likes: arrayUnion(uid),
                });

                post.likes.push(uid);
            } catch (error) {
                console.error("Error updating likes: ", error);
            }
        },

        async unlikePost(post) {
            try {
                const uid = auth.currentUser.uid;

                const postRef = doc(db, "posts", post.id);

                // Unlike the post by removing the user's UID from the likes array
                await updateDoc(postRef, {
                    likes: arrayRemove(uid),
                });

                const index = post.likes.indexOf(uid);
                if (index > -1) {
                    post.likes.splice(index, 1);
                }
            } catch (error) {
                console.error("Error updating likes: ", error);
            }
        },

        async reportPost(post) {
            try {

                console.log(post)
                const uid = auth.currentUser.uid;

                const postRef = doc(db, "posts", post.id);

                // Like the post by adding the user's UID to the likes array
                await updateDoc(postRef, {
                    reports: arrayUnion(uid),
                });

                post.reports.push(uid);
            } catch (error) {
                console.error("Error adding report: ", error);
            }
        },
        async deletePost(post) {
            try {
                
                const postRef = doc(db, "posts", post.id);

                // Like the post by adding the user's UID to the likes array
                await updateDoc(postRef, {
                    isDeleted: true,
                });

                post.isDeleted = true;
            } catch (error) {
                console.error("Error adding report: ", error);
            }
        },


    },
};
</script>
  
<style scoped>
h1 {
    width: 15%;
    margin-left: 50%;
    color: #4a6fa5;
}

.class-feed {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin-top: 30px;
}

.post-container {
    height: 61%;
    overflow-y: scroll;
    margin-top: 20px;
    background-color: #e0e1dd;
    width: 40%;
    position: absolute;
    margin-left: 36%;
}

.post {
    border: solid;
    border-color: #4a6fa5;
    border-width: 5px;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 25px;
}

.post-header {
    display: flex;
}

::-webkit-scrollbar {
    display: none;
}

.avatar {
    width: 50px;
    height: 50px;
    margin-right: 10px;
    border-radius: 50%;
}

.author-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: black;
}

.author-name {
    font-weight: bold;
    color: black;
}

.post-date {
    color: black;
    font-size: 14px;
    font-style: italic;
}

.post-content {
    margin-top: 2%;
    color: black;
    text-align: center;
}

.mdi-heart-outline {
    margin-left: -5px;
    margin-top: -3px;
}

.mdi-heart {
    margin-left: -5px;
    margin-top: -3px;
}

.v-btn .mdi-heart-outline:hover {

    margin-top: -3px;
    color: rgb(180, 25, 25);
    transform: scale(1.1);
}

.v-btn .mdi-heart:hover {

    margin-top: -3px;
    transform: scale(1.1);
}
</style>