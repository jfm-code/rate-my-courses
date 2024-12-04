<template>
  <div >
    <NavigationBar></NavigationBar>
    <div class="course-info" >
      <div>
        <h1><a href="https://www.uml.edu/catalog/courses/COMP/1020">{{ course_name }}</a></h1>
        <div>
          <span>Data structures</span>
          <span>Algorithms</span>
          <span>Performance analysis</span>
          <span>Extensive lab work</span>
        </div>
      </div>
      <div>
        <div class="avg-score">{{ calculateAverageRating() }}</div>
        <div class="total-score">/ 5</div>
      </div>
    </div>
    <div class="read-write-section"> 
      <div class="course-rating">
        <div v-for="review in reviews" :key="review.id">
          <div>
            <span>RATING</span>
            <span>{{ review.rating }}</span>
          </div>
          <div>
            <span>REVIEW</span>
            <span>{{ review.comment }}</span>
            <button class="delete-button" @click="deleteReview(review.id)">
              <i class="fas fa-trash"></i>
            </button>

          </div>
        </div>
      </div>
      <div class="write-rating">
        <p style="margin-bottom: 0px;">Write your review for {{ course_name }}</p>
        <div class="rate-container">
          <span @click="rate(1)" class="rate-box" id="box1" style="border-radius: 15px 3px 3px 15px; width: 15px;">1</span>
          <span @click="rate(2)" class="rate-box" id="box2">2</span>
          <span @click="rate(3)" class="rate-box" id="box3">3</span>
          <span @click="rate(4)" class="rate-box" id="box4">4</span>
          <span @click="rate(5)" class="rate-box" id="box5" style="border-radius: 3px 15px 15px 3px; width: 15px;">5</span>
        </div>
        <textarea @keyup.enter="postReview" v-model="newReview.comment" rows="9" cols="45" placeholder="What did you like / dislike about this course?"></textarea>
        <input type="submit" value="Post" @click="postReview">
      </div>
    </div>
    <FooterSection></FooterSection>
  </div>
</template>

<script>
import axios from 'axios';
import NavigationBar from './NavigationBar.vue';
import FooterSection from './FooterSection.vue';
export default {
  name: 'ReviewPage',
  components: {
    NavigationBar,
    FooterSection
  },
  data() { // Vue's reactivity system tracks changes to properties in the data
    return {
      course_name: '',
      reviews: [], // when reviews is updated, Vue re-renders the component
      newReview: {
        rating: null,
        comment: '',
      },
    };
  },
  beforeRouteEnter(to, from, next) { // fetch data when entering the route. Has to be outside of the methods functions
      //can not use this here because of scope. Use vm instead.
      next(vm => {
        vm.course_id = vm.$route.params.id;
        vm.course_name = vm.$route.params.name;
        vm.getReview(vm.$route.params.id);
      });
  },
  methods: {
    // fetch all reviews data of that course_id
    // use async because we need to wait for API response
    async getReview(course_id) { 
      try {
        const response = await axios.get(`${process.env.VUE_APP_API_URL}/reviews/${course_id}`);
        this.reviews = response.data.map(review => ({
          id: review.review_id,
          rating: review.rating,
          comment: review.comment,
        }));
      } catch(error) {
        console.error('Error fetching reviews:', error);
      }
    },
    // create a new review for the course
    async postReview() {
      // validate that both rating and comment are present
      if (!this.newReview.rating || !this.newReview.comment.trim()) {
        alert("Please provide both a rating and a comment.");
        return;
      }
      // send request by calling API
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_API_URL}/reviews/${this.$route.params.id}`, //params.id will be the course id
          {
            rating: this.newReview.rating,
            comment: this.newReview.comment,
          }
        );
        // add the new review to the reviews list to update the UI
        this.reviews.push({
          id: response.data.review_id || Date.now(), // use API response ID or a temporary one
          rating: this.newReview.rating,
          comment: this.newReview.comment,
        });
        // clear the input fields
        this.newReview.rating = null;
        this.newReview.comment = '';
        // reset the rating background
        document.querySelectorAll('.rate-box').forEach(box => {
          box.classList.remove('selected');
        });
        alert("Review added successfully.");

      } catch (error) {
        console.error('Error posting review:', error);
        alert("Failed to add review. Please try again.");
      }
    },
    // delete a specific review
    async deleteReview(review_id) {
      try {
        await axios.delete(`${process.env.VUE_APP_API_URL}/reviews/${review_id}`);
        // Update UI after deletion
        this.reviews = this.reviews.filter(review => review.id !== review_id);
      } catch (error) {
        console.error('Error deleting review:', error);
      }
    },
    calculateAverageRating() {
      if(this.reviews.length == 0) {
        return 0;
      }
      else {
        let sum = 0;
        this.reviews.forEach(review => {
          sum += review.rating;
        });
        return (sum / this.reviews.length).toFixed(1); // rounded to 1 decimal place;
      }
    },
    rate(rating) {
      this.newReview.rating = rating;
      document.querySelectorAll('.rate-box').forEach(box => {
          box.classList.remove('selected');
      });
      for (let i = 1; i <= rating; i++) {
          document.getElementById('box' + i).classList.add('selected');
      }
    },
  }
}
</script>

<style scoped>
* {
  
}
h1 {
  font-size: 40px;
}
a {
  text-decoration: none;
  color: darkcyan;
  position: relative;

}
h1 a::after {
  content: "";
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 0;
  height: 3px;
  background-color: currentColor; /* Use the text color for underline */
  transition: width 0.3s ease, left 0.3s ease;
}
h1 a:hover::after {
  width: 100%;
  left: 0;
}
.course-info {
  display: grid;
  grid-template-columns: 60% 40%;
  margin:0px 50px 0px 50px;
}
.course-info > div:nth-child(1) {
  padding: 20px;
  margin-left:20px;
}
span {
  margin: 0px 15px 0px 15px;
  font-size:large
}
.course-info > div:nth-child(2) {
  display: grid;
  grid-template-columns: 65% 35%;
  width: 40%;
  justify-self: center;
  padding: 40px 20px 0px 0px;
  margin: 50px 80px 50px 0px;
  height: 120px;
  color:white;
  background-color: #5f9ea0;
  border-radius: 10px;
}
.avg-score {
  font-size: 70px;
  justify-self: end;
}
.total-score {
  font-size: 30px;
  justify-self:left;
  margin-left:20px;
  padding-top:8px;

}
.read-write-section {
  display: flex;
  margin: 20px 140px 5px 140px;
  gap: 4rem;
}
.course-rating {
  width: 60%;
  justify-self: start;
}
.course-rating > div {
  display: grid;
  grid-template-columns: 25% 75%;
  border-radius: 10px;
}
.course-rating > div > div {
  display: flex;
  flex-direction: column;
  margin-bottom: 35px;
}
.course-rating > div > div:nth-child(1) {
  background-color:cadetblue;
  border-radius: 10px 0px 0px 10px;
}
.course-rating > div > div:nth-child(2) {
  border-style: solid solid solid hidden;
  border-color: cadetblue;
  border-radius: 0px 10px 10px 0px;
}
.course-rating > div > div:nth-child(1) > span:nth-child(1) {
  color: white;
  margin-bottom: 0px;
}
.course-rating > div > div:nth-child(1) > span:nth-child(2) {
  color: white;
  border-radius: 10px;
  margin:0px 50px 10px 50px;
  padding-left:15px;
  font-size:70px;
}
.course-rating > div > div > span:nth-child(1) {
  font-weight: bold;
  font-size: larger;
  padding: 20px 0px 0px 0px;
}
.course-rating > div > div > span:nth-child(2) {
  font-size: medium;
  padding: 25px;
  text-align: justify;
}
.write-rating {
  border-style: solid;
  width: 40%;
  height: 100%;
  border-radius: 10px;
  border-color: cadetblue;
}
.write-rating > p {
  font-weight: bold;
  font-size: larger;
  text-transform: capitalize;
}
.rate-container {
  margin: 12px 0px 12px 0px;
  padding: 8px 0px 8px 0px;
  display: flex;
  justify-content: center;
  gap: 5px;
}
.rate-box {
  height: inherit;
  padding: 7px 12px;
  background-color: #d8eced;
  border-radius: 3px;
  margin:0px;
  cursor: pointer;
}
.rate-box:hover {
  background-color:rgb(123, 194, 196);
  color:white;
}
.rate-box.selected {
  background-color:darkcyan;
  color:white;
}
textarea {
  padding: 20px;
  margin: 0px 15px 5px 15px;
  border: 0px;
  border-radius: 3px;
  justify-self: center;
  font-family: Arial, sans-serif;
  font-size: 16px;
  color: #333;
  resize: none;
  background-color:#d8eced;
  outline: none;
}
.write-rating > input {
  margin: 10px 0px 18px 0px;
  padding: 8px 20px;
  border: 2px solid cadetblue;
  border-radius: 5px;
  background-color: cadetblue;
  color: white;
  font-size: 16px;
  cursor: pointer;
}
.write-rating > input:hover {
  border-color: darkcyan;
  background-color: darkcyan;
}
.delete-button {
  background-color:white;
  color: cadetblue;
  padding: 6px 4px;
  margin-left:470px;
  margin-top: 20px;
  font-size: 16px;
  border:none;
  border-radius: 5px;
  cursor: pointer;
  width: 35px;
  height: 35px;
}
.delete-button:hover {
  background-color: #d8eced;
  color:darkcyan;
}

</style>
