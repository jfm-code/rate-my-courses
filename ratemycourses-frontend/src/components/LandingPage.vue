<template>
  <div>
    <NavigationBar></NavigationBar>
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
    <FooterSection></FooterSection>
  </div>
</template>

<script>
import axios from 'axios';
import NavigationBar from './NavigationBar.vue';
import FooterSection from './FooterSection.vue'
export default {
  name: 'LandingPage',
  components: {
    NavigationBar,
    FooterSection
  },
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
  height: 43.6vh;
  background-attachment: fixed;
  padding: 100px 0px 100px 0px;
  color:white;
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
