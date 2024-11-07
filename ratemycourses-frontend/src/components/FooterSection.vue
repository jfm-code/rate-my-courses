<template>
    <div class="footer">
      <div> 
        <a href="#">Help</a>
        <a href="#">Site Guidelines</a>
      </div>
      <div> 
        <span>© 2024 Rate My Courses. All Rights Reserved</span>
      </div>
    </div>
</template>

<script>
export default {
    name: 'FooterSection',
};
</script>

<style scoped>
.footer {
  height: 50px;
  display: flex;
  flex-direction: column;
  padding: 25px 0px 25px 0px;
  gap: 15px;
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
</style>