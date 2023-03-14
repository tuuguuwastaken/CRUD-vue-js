<template>
    <div class="container boxx">
        <form @submit.prevent="createPost">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" v-model="post.title">
            <br>
            <label for="body">Body:</label>
            <textarea id="textbody" name="body" v-model="post.body"></textarea>
            <br>
            <button type="submit">Create Post</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name:'upload-main',
    components:{

    },
    data() {
        return {
            post: {
                title: '',
                body: ''
            }
        }
    },
    methods: {
        createPost() {
            console.log(this.post)
            axios.post('http://127.0.0.1:5000/upload', {
                    data1: this.post.title,
                    data2: this.post.body
                })
                .then(response => {
                    console.log(response.data);
                    alert('Post created successfully');
                })
                .catch(error => {
                    console.log(error);
                    alert('Failed to create post');
                })
                .finally(function(){
                    this.$router.push('/')
                })
        }
    }
}
</script>

<style scoped>
    .boxx{
        background-color:#b9e3ff;
    }
    label{
        font-size:2.5rem;
    }
    #title {
        width: 100%;
        height: 40px;
        font-size: 16px;
        padding: 10px;
        border: 1px solid #4290c4;
        border-radius: 4px;
        box-sizing: border-box;
    }
    #textbody{
        width: 100%;
        height: 200px;
        font-size: 16px;
        padding: 10px;
        border: 1px solid #4290c4;
        border-radius: 4px;
        box-sizing: border-box;
    }
</style>