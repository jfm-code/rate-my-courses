<template>
    <div class="nav">
      <img src="../assets/rate-my-courses-logo.png" @click="$router.push({ path: '/' })" style="cursor: pointer;"/>
      <a href="#">Login</a>
      <a href="#">Sign Up</a>
    </div>
</template>

<script>
export default {
  name: 'NavigationBar',
};
</script>

<style scoped>
.nav {
  height: 50px;
  display: flex;
  padding: 22.5px 50px 22.5px 0px;
  gap: 25px;
  justify-content: end;
}
.nav > img {
  margin-right:975px;
  justify-self: baseline;
  /* border-style: dotted; */
}
.nav > a {
  border-style: solid;
  border-color: cadetblue;
  background: cadetblue;
  border-radius: 10px;
  height:20px;
  width: 65px;
  padding: 8px 6px 5px 6px;
  justify-items: center;
  text-decoration: none;
  color: white;
}
.nav > a:hover {
  background-color: darkcyan;
  border-color:darkcyan;
}
</style>