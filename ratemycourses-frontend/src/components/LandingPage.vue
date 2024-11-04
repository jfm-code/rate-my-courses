<template>
  <div>
    <div class="nav">
      <a href="#">Login</a>
      <a href="#">Sign Up</a>
    </div>
    <div class="container">
      <h1>Rate My Courses</h1>
      <h2>Please choose an UML CS course to see the rating</h2>
      <div class="course-list" v-if="courses.length > 0">
        <div class="card" v-for="course in courses" :key="course.id" @click="goToReview(course.id, course.name)">
          <p>
            <span>{{ course.name }}</span>
          </p>
        </div>
      </div>
    </div>
    <div class="footer">
      <div> 
        <a href="#">Help</a>
        <a href="#">Site Guidelines</a>
      </div>
      <div> 
        <span>© 2024 Rate My Courses. All Rights Reserved</span>
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
    goToReview(id, name) { // Route to /:id/reviews when the form is submitted
    this.$router.push({path: `${name}/${id}/reviews`, state: { name }});
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

<style scoped>
.container {
  background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.8)), url('../umasslowell.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  height: 43vh;
  background-attachment: fixed;
  padding: 100px 0px 100px 0px;
  color:white;
}
.nav {
  height: 50px;
  display: flex;
  padding: 25px 50px 20px 0px;
  gap: 25px;
  justify-content: end;
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
.footer {
  height: 50px;
  display: flex;
  flex-direction: column;
  padding-top: 30px;
  gap: 20px;
  justify-content: center;
  color: darkcyan;
}
.footer > div:nth-child(1) {
  display: flex;
  gap: 20px;
  justify-content: center;
}
.footer > div > a {
  text-decoration: none;
  color: darkcyan;
  position: relative;
}
.footer > div > a::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: -1px;
  width: 0;
  height: 2px;
  background-color: currentColor; /* Use the text color for underline */
  transition: width 0.3s ease, left 0.3s ease;
}
.footer > div > a:hover::after {
  width: 100%;
  left: 0;
}
h1 {
  font-size: 60px;
  background: linear-gradient(white, white, rgb(111, 182, 184), cadetblue);
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.course-list {
  display: grid;
  grid-template-columns: auto auto auto auto;
  justify-self: center;
}
.card {
  background-color: white;
  padding:0px 10px 0px 10px;
  margin-left: 20px;
  margin-top: 30px;
  margin: 30px 0px 30px 20px;
  color: darkcyan;
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
