<template>
<div>
  <div>
    <h1>Computing I</h1>
    <p>Average rating: 9/10</p>
  </div>
  <div class="comment_sections">
    <div id ="id of this comment from databse" class="comments">
          <span class="rating">Rating: <span>7</span></span><br>
          <div>some comments here</div>
    </div>
    <div id ="id2 of this comment from databse" class="comments">
        <span class="rating">Rating: <span>6</span></span><br>
        <div>some comments here</div>
    </div>
  </div>
</div>

</template>

<script>
export default {
  name: 'ReviewPage',
}
</script>

<style scoped>
.comment_sections {
    display: flex; /* Enables Flexbox */
    justify-content: space-between; /* Distributes space between items */
    justify-self: center;
    flex-direction: column;
     /* Space between items */
    align-items: center; /* Centers items vertically */
    width: 60vw;
}
.comments {
  width: 100%;
  height: auto;
  background-color: #EFE8E8;
  flex: 1; /* Items grow equally */
  margin-top: 10px;
  border-radius: 5px;
}

.rating {
  background-color: #00FFFF;
  padding: 4px;
  border-radius: 6px;
  margin-top: 10px;

}
</style>
