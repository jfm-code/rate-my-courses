<template>
  <div>
    <h1>Find My Courses</h1>
    <h3>Please choose a CS course to see review</h3>
    <!-- Prevent the default form submission behavior because we don't want the form to 
    reload the page; instead, we want Vue Router to handle the navigation. -->
    <form @submit.prevent="goToReview">
      <input type="text" id="fname" name="fname"><br>
      <input type="submit" value="Submit">
    </form>
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

</style>
