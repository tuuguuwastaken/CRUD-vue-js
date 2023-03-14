<template>
    <button @click="$router.push(String(this.path)); this.action" :style="{ background: color }" class="btn">{{ text }}</button>
</template>


<script>
    export default{
        name: 'Button-main',
        props:{
            text: String,
            color:String,
            path: {
                type: String,
                default: "/"
            },
            action: String
        },
        methods:{
            onclick(){
                console.log('click');
            }
        }
    }
</script>