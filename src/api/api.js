import { collection, query, where, getDocs } from "firebase/firestore";
import { db } from "@/firebase";

export const fetchPosts = async () => {
  const postRef = collection(db, "posts");
  const q = query(postRef, where("isDeleted", "==", false));
  const querySnapshot = await getDocs(q);
  const postsArray = querySnapshot.docs.map((doc) => ({
    id: doc.id,
    ...doc.data(),
  }));
  return postsArray;
};