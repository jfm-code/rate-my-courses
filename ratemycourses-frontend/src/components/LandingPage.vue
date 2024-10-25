<template>
  <div class="container">
    <h1>Rate My Courses</h1>
    <h2>Please choose an UML CS course to see review</h2>
    <div class="course-list"> 
      <div @click="goToReview" class="card">
        <p>
          <span>COMP.1020</span>
          <span>Computing II</span>
        </p>
      </div>
      <div @click="goToReview" class="card">
        <p>
          <span>COMP.1020</span>
          <span>Computing II</span>
        </p>
      </div>
      <div @click="goToReview" class="card">
        <p>
          <span>COMP.2010</span>
          <span>Computing III</span>
        </p>
      </div>
      <div @click="goToReview" class="card">
        <p>
          <span>COMP.2030</span>
          <span>Assembly Prog. Language</span>
        </p>
      </div>
      <div @click="goToReview" class="card">
        <p>
          <span>COMP.2040</span>
          <span>Computing IV</span>
        </p>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  props: {
    msg: String
  },
  methods: {
    goToReview() {
      // Route to /course when the form is submitted
      this.$router.push('/course');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('../umasslowell.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  height: 100vh;
  background-attachment: fixed;
  padding: 100px 0px 100px 0px;
  color:white;
}
.course-list {
  display: grid;
  grid-template-columns: auto auto auto auto;
  justify-self: center;
}
.card {
  background-color: white;
  padding:2px 10px 2px 10px; /* top, right, bottom, left */
  margin-left: 20px;
  margin-top: 30px;
  margin: 30px 0px 30px 20px;
  color: darkslategray;
  user-select: none;
  border-radius: 10px;
  border-style: solid;
  border-color:cadetblue;
}
.card:hover {
  background-color:cadetblue;
  color: white;
}
.card > p > span {
  margin:5px;
}
</style>
