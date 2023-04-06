<template>
    <div class="Class-feed">
        <h1>Class Feed</h1>
        <div class="post-container">
            <v-card v-for="post in posts" :key="post.uid" class="post" variant="outlined" :title="`${ post.firstName } ${ post.lastName }`">
                <template v-slot:prepend>
                    <v-avatar color="grey-darken-3"
                        image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"></v-avatar>
                </template>
                <v-card-text class="text-h6">
                    {{ post.content }}
                </v-card-text>
                <v-card-actions>
                    <v-list-item class="w-100">

                        <div class="justify-self-start">
                            <span class="subtitle me-2">[section] </span>
                        </div>
                        <template v-slot:append>
                            <div class="justify-self-end">
                                <span class="subtitle me-2">{{ formatDate(post.PostDate) }}</span>
                                <span class="me-2">·</span>
                                <span class="subtitle me-2">{{ formatTime(post.PostDate) }}</span>
                                <span class="me-1">·</span>
                                <v-btn class="me-1" icon>
                                    <v-icon>mdi-heart-outline</v-icon>
                                </v-btn>
                                <span class="subheading ml-0">{{ post.likes }}</span>

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
import { collection, query, where, getDocs } from "firebase/firestore";
import { db } from "@/firebase";
import { useRoute } from "vue-router";

export default {
    name: "ClassFeed",
    setup() {
        const route = useRoute();
        const classPrefix = (route.params.classPrefix);
        const classNumber = (route.params.classNumber);
        const posts = ref([]);
        const error = ref(null);
        const fetchPosts = async () => {
            try {
                const postRef = collection(db, "posts");
                const q = query(postRef,
                    where("classPrefix", "==", classPrefix),
                    where("classNumber", "==", classNumber),
                    where("postType", "==", "post")
                );
                const querySnapshot = await getDocs(q);
                const postsArray = querySnapshot.docs.map((doc) => ({
                    id: doc.id,
                    ...doc.data(),
                }));
                posts.value = postsArray;
                posts.value.sort((a, b) => b.PostDate - a.PostDate);
                console.log(posts.value);
            } catch (err) {
                error.value = err.message;
            }
        };
        onMounted(() => {
            fetchPosts();
        });

        return { posts, error };
    },
    methods: {
        formatTime(timestamp) {
            const date = timestamp.toDate();
            const hours = date.getHours();
            const minutes = date.getMinutes().toString().padStart(2, '0');
            const ampm = hours >= 12 ? 'PM' : 'AM';
            const twelveHours = hours % 12 || 12;
            return `${twelveHours}:${minutes} ${ampm}`;
        },
        formatDate(timestamp) {
            const date = timestamp.toDate();
            const options = { month: 'numeric', day: 'numeric', year: '2-digit' };
            return new Intl.DateTimeFormat('en-US', options).format(date);
        }
    },
    computed: {
        displayedPosts() {
            return this.posts.slice(0, this.maxPosts);
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
</style>