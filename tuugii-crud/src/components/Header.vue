<template>
    <header>
        <h1>{{title}}</h1>
        <Button text="Add Task" color="green"/>
        <Button text="Upload new post" color="blue" path="/upload"/>
    </header>
</template>

<script>
import Button from './Button'
export default {
    name: 'Header-top',
    props:{
        title: String,
    },
    components: {
        Button,
    }
}
</script>

<style scoped>
    header{
        display:flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
</style>