<template>
  <div class="container">
    <h1>Rate My Courses</h1>
    <h2>Please choose an UML CS course to see review</h2>
    <div class="course-list" v-if="courses.length > 0">
      <div class="card" v-for="course in courses" :key="course.id" @click="goToReview(course.id)">
        <p>
          <span>{{ course.name }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LandingPage',
  props: {
    msg: String
  },
  data() { // Vue's reactivity system tracks changes to properties in the data
    return {
      courses: [] // when courses is updated, Vue re-renders the component
    };
  },
  methods: {
    goToReview() { // Route to /course when the form is submitted
      this.$router.push('/course');
    },
    async fetchCourseData() { // use async because we need to wait for API response
      try {
        const response = await axios.get(`${process.env.VUE_APP_API_URL}/courses`);
        this.courses = Object.entries(response.data).map(([id, name]) => ({
          id,
          name
        }));
      } catch(error) {
        console.error('Error fetching courses:', error);
      }
    }
  },
  beforeRouteEnter(to, from, next) { // fetch data when entering the route. Prevent delay on page load when using mounted()
    next(vm => {
      vm.fetchCourseData(); 
    });
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
