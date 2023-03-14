<template>
    <div class="container">
        <Header title="Hello welcome" />
		<div v-for="post in posts" :key="post.id">
			<h1>{{ post[0] }} : {{ post[1] }}</h1>
			<p>{{ post[2] }}</p>
			<hr>
		</div>
    </div>
</template>

<script>
import Header from "@/components/Header.vue";
import axios from 'axios'
export default {
    name: "HomeView",
    components: {
        Header
    },
    data() {
        return {
            message: "",
			posts: []
        }
    },
    mounted() {
		axios.get('http://127.0.0.1:5000/api/posts')
			.then(res =>{
				this.posts = res.data;
			})
			.catch(err =>{
				alert(err)
			})
	}
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: "Poppins", sans-serif;
}
.container {
    max-width: 900px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    border: 1px solid steelblue;
    padding: 30px;
    border-radius: 5px;
}
.btn {
    display: inline-block;
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
}
.btn:focus {
    outline: none;
}
.btn:active {
    transform: scale(0.98);
}
.btn-block {
    display: block;
    width: 100%;
}
</style>
