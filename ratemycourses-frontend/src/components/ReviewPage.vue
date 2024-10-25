<template>
  <div>
    <div class="course-info">
      <div>
        <h1><a href="https://www.uml.edu/catalog/courses/COMP/1020">COMP.1020 Computing II</a></h1>
        <div>
          <span>Data structures</span>
          <span>Algorithms</span>
          <span>Performance analysis</span>
          <span>Extensive lab work</span>
        </div>
      </div>
      <div>
        <div class="avg-score">7.8</div>
        <div class="total-score">/  10</div>
      </div>
    </div>
    <div class="course-rating">
      <div>
        <div>
          <span>RATING</span>
          <span>8</span>
        </div>
        <div>
          <span>REVIEW</span>
          <span>Computing II focuses on the implementation and applications of data structures, including arrays, linked lists, stacks, queues, trees, binary trees, binary search trees, heaps, graphs, and hash tables. Recursive approaches are used. Performance analysis is discussed. Attention is paid to programming style, documentation, and testing. This course includes extensive laboratory work. Effective Fall 2013, Co-req: Computing 2 Lab.</span>
        </div>
      </div>
      <div>
        <div>
          <span>RATING</span>
          <span>6</span>
        </div>
        <div>
          <span>REVIEW</span>
          <span>Computing II focuses on the implementation and applications of data structures, including arrays, linked lists, stacks, queues, trees, binary trees, binary search trees, heaps, graphs, and hash tables. Recursive approaches are used. Performance analysis is discussed. Attention is paid to programming style, documentation, and testing. This course includes extensive laboratory work. Effective Fall 2013, Co-req: Computing 2 Lab.</span>
        </div>
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
  margin:50px;
}
.course-info > div:nth-child(1) {
  padding: 50px;
  margin-left:20px
}
span {
  margin: 0px 15px 0px 15px;
  font-size:large
}
.course-info > div:nth-child(2) {
  display: grid;
  grid-template-columns: 60% 40%;
  width: 40%;
  justify-self: center;
  padding: 35px 20px 0px 0px;
  margin: 50px 0px 50px 0px;
  height: 120px;
  color:white;
  background-color: cadetblue;
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
.course-rating {
  width: 50%;
  justify-self: center;
}
.course-rating > div {
  display: grid;
  grid-template-columns: 25% 75%;
  border-radius: 10px;
}
.course-rating > div > div {
  display: flex;
  flex-direction: column;
  margin-bottom: 40px;
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
  margin:20px 50px 20px 50px;
  padding-left:25px;
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
</style>
