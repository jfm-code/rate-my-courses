<template>
  <div>
    <NavigationBar></NavigationBar>
    <div class="container">
      <h1>Rate My Courses</h1>
      <h2>Please choose an UML CS course to see the rating</h2>
      <div class="add-course">
        <input type="text" id="add-course-field" placeholder="Add a course here..." v-model="newCourseName">
        <input type="submit" value="Create" @click="addCourse">
      </div>
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
      newCourseName: '',
      courses: [] // when courses is updated, Vue re-renders the component
    };
  },
  methods: {
    goToReview(id, name) { // Route to /:id/reviews when the form is submitted
    this.$router.push({path: `${name}/${id}/reviews`, state: { name }});
    },
    async fetchCourseData() { // use async because we need to wait for API response
      try {
        const response = await axios.get(`${process.env.VUE_APP_API_URL}/courses/`);
        this.courses = Object.entries(response.data).map(([id, name]) => ({
          id,
          name
        }));
      } catch(error) {
        console.error('Error fetching courses:', error);
      }
    },
    async addCourse() {
      if (!this.newCourseName.trim()) {
        alert("Please enter a valid course name.")
        return
      }

      try {
        const response = await axios.post(`${process.env.VUE_APP_API_URL}/courses/${this.newCourseName}/create`);
        console.log(response);
        this.newCourseName = ''; // Clear input field
        this.fetchCourseData(); // Refresh the course list
      } catch (error) {
        console.error('Error creating course:', error);
        alert(error.response?.data?.message || 'Failed to create course.');
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
  padding: 50px 0px 130px 0px;
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
  grid-template-columns: auto auto auto auto auto auto;
  justify-self: center;
  width: 70%;
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
.add-course {
  margin:50px 0px 20px 0px;
}
.add-course > input:nth-child(1) {
  padding: 10px 20px;
  background-color: transparent;
  user-select: none;
  border-color:cadetblue;
  color: white;
  border-style:solid none solid solid;
  border-radius: 10px 0px 0px 10px;
  font-size: medium;
}
.add-course > input:nth-child(1):focus {
  outline: none;
}
input::placeholder {
  color: white;
}
.add-course > input:nth-child(2) {
  border-style: solid;
  border-color: cadetblue;
  background: cadetblue;
  border-radius: 0px 10px 10px 0px;
  padding: 10px 15px;
  justify-items: center;
  text-decoration: none;
  color: white;
  font-size: medium;
}
.add-course > input:nth-child(2):hover {
  background-color: darkcyan;
  border-color:darkcyan;
  cursor: pointer;
}
</style>
