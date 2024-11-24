(function(){"use strict";var e={674:function(e,t,n){var r=n(5130),o=n(6768);const a={id:"app"};function s(e,t,n,r,s,i){const c=(0,o.g2)("router-view");return(0,o.uX)(),(0,o.CE)("div",a,[(0,o.bF)(c)])}var i={name:"App"},c=n(1241);const u=(0,c.A)(i,[["render",s],["__scopeId","data-v-896c0768"]]);var l=u,d=n(1387),v=n(4232);const p={class:"container"},f={key:0,class:"course-list"},k=["onClick"];function h(e,t,n,r,a,s){const i=(0,o.g2)("NavigationBar"),c=(0,o.g2)("FooterSection");return(0,o.uX)(),(0,o.CE)("div",null,[(0,o.bF)(i),(0,o.Lk)("div",p,[t[0]||(t[0]=(0,o.Lk)("h1",null,"Rate My Courses",-1)),t[1]||(t[1]=(0,o.Lk)("h2",null,"Please choose an UML CS course to see the rating",-1)),a.courses.length>0?((0,o.uX)(),(0,o.CE)("div",f,[((0,o.uX)(!0),(0,o.CE)(o.FK,null,(0,o.pI)(a.courses,(e=>((0,o.uX)(),(0,o.CE)("div",{class:"card",key:e.id,onClick:t=>s.goToReview(e.id,e.name)},[(0,o.Lk)("p",null,[(0,o.Lk)("span",null,(0,v.v_)(e.name),1)])],8,k)))),128))])):(0,o.Q3)("",!0)]),(0,o.bF)(c)])}n(4114);var g=n(4373),m=n.p+"img/rate-my-courses-logo.55a5a025.png";const L={class:"nav"};function b(e,t,n,r,a,s){return(0,o.uX)(),(0,o.CE)("div",L,[(0,o.Lk)("img",{src:m,onClick:t[0]||(t[0]=t=>e.$router.push({path:"/"})),style:{cursor:"pointer"}}),t[1]||(t[1]=(0,o.Lk)("a",{href:"#"},"Login",-1)),t[2]||(t[2]=(0,o.Lk)("a",{href:"#"},"Sign Up",-1))])}var w={name:"NavigationBar"};const y=(0,c.A)(w,[["render",b],["__scopeId","data-v-7cf21b16"]]);var x=y;const C={class:"footer"};function _(e,t,n,r,a,s){return(0,o.uX)(),(0,o.CE)("div",C,t[0]||(t[0]=[(0,o.Lk)("div",null,[(0,o.Lk)("a",{href:"#"},"Help"),(0,o.Lk)("a",{href:"#"},"Site Guidelines")],-1),(0,o.Lk)("div",null,[(0,o.Lk)("span",null,"© 2024 Rate My Courses. All Rights Reserved")],-1)]))}var E={name:"FooterSection"};const O=(0,c.A)(E,[["render",_],["__scopeId","data-v-ba3d005e"]]);var R=O,A={name:"LandingPage",components:{NavigationBar:x,FooterSection:R},props:{msg:String},data(){return{courses:[]}},methods:{goToReview(e,t){this.$router.push({path:`${t}/${e}/reviews`,state:{name:t}})},async fetchCourseData(){try{const e=await g.A.get("http://127.0.0.1:5000/courses");this.courses=Object.entries(e.data).map((([e,t])=>({id:e,name:t})))}catch(e){console.error("Error fetching courses:",e)}}},beforeRouteEnter(e,t,n){n((e=>{e.fetchCourseData()}))}};const S=(0,c.A)(A,[["render",h],["__scopeId","data-v-48d9a6f2"]]);var F=S;const j={class:"course-info"},I={href:"https://www.uml.edu/catalog/courses/COMP/1020"},P={class:"avg-score"},X={class:"read-write-section"},M={class:"course-rating"},T={class:"write-rating"},$={style:{"margin-bottom":"0px"}},B={class:"rate-container"};function N(e,t,n,r,a,s){const i=(0,o.g2)("NavigationBar"),c=(0,o.g2)("FooterSection");return(0,o.uX)(),(0,o.CE)("div",null,[(0,o.bF)(i),(0,o.Lk)("div",j,[(0,o.Lk)("div",null,[(0,o.Lk)("h1",null,[(0,o.Lk)("a",I,(0,v.v_)(a.course_name),1)]),t[5]||(t[5]=(0,o.Lk)("div",null,[(0,o.Lk)("span",null,"Data structures"),(0,o.Lk)("span",null,"Algorithms"),(0,o.Lk)("span",null,"Performance analysis"),(0,o.Lk)("span",null,"Extensive lab work")],-1))]),(0,o.Lk)("div",null,[(0,o.Lk)("div",P,(0,v.v_)(s.calculateAverageRating()),1),t[6]||(t[6]=(0,o.Lk)("div",{class:"total-score"},"/ 5",-1))])]),(0,o.Lk)("div",X,[(0,o.Lk)("div",M,[((0,o.uX)(!0),(0,o.CE)(o.FK,null,(0,o.pI)(a.reviews,(e=>((0,o.uX)(),(0,o.CE)("div",{key:e.id},[(0,o.Lk)("div",null,[t[7]||(t[7]=(0,o.Lk)("span",null,"RATING",-1)),(0,o.Lk)("span",null,(0,v.v_)(e.rating),1)]),(0,o.Lk)("div",null,[t[8]||(t[8]=(0,o.Lk)("span",null,"REVIEW",-1)),(0,o.Lk)("span",null,(0,v.v_)(e.comment),1),t[9]||(t[9]=(0,o.Lk)("button",{class:"delete-button"},[(0,o.Lk)("i",{class:"fas fa-trash"})],-1))])])))),128))]),(0,o.Lk)("div",T,[(0,o.Lk)("p",$,"Write your review for "+(0,v.v_)(a.course_name),1),(0,o.Lk)("div",B,[(0,o.Lk)("span",{onClick:t[0]||(t[0]=e=>s.rate(1)),class:"rate-box",id:"box1",style:{"border-radius":"15px 3px 3px 15px",width:"15px"}},"1"),(0,o.Lk)("span",{onClick:t[1]||(t[1]=e=>s.rate(2)),class:"rate-box",id:"box2"},"2"),(0,o.Lk)("span",{onClick:t[2]||(t[2]=e=>s.rate(3)),class:"rate-box",id:"box3"},"3"),(0,o.Lk)("span",{onClick:t[3]||(t[3]=e=>s.rate(4)),class:"rate-box",id:"box4"},"4"),(0,o.Lk)("span",{onClick:t[4]||(t[4]=e=>s.rate(5)),class:"rate-box",id:"box5",style:{"border-radius":"3px 15px 15px 3px",width:"15px"}},"5")]),t[10]||(t[10]=(0,o.Lk)("textarea",{rows:"9",cols:"45",placeholder:"What did you like / dislike about this course?"},null,-1)),t[11]||(t[11]=(0,o.Lk)("input",{type:"submit",value:"Post"},null,-1))])]),(0,o.bF)(c)])}var D={name:"ReviewPage",components:{NavigationBar:x,FooterSection:R},data(){return{course_name:"",reviews:[]}},methods:{async getReviewsData(e){try{const t=await g.A.get(`http://127.0.0.1:5000/reviews/${e}`);this.reviews=Object.entries(t.data).map((([e,t])=>({id:e,rating:t.rating,comment:t.comment})))}catch(t){console.error("Error fetching reviews:",t)}},calculateAverageRating(){if(0==this.reviews.length)return 0;{let e=0;return this.reviews.forEach((t=>{e+=t.rating})),(e/this.reviews.length).toFixed(1)}},rate(e){document.querySelectorAll(".rate-box").forEach((e=>{e.classList.remove("selected")}));for(let t=1;t<=e;t++)document.getElementById("box"+t).classList.add("selected")}},beforeRouteEnter(e,t,n){console.log("finish"),n((e=>{e.getReviewsData(e.$route.params.id),e.course_name=e.$route.params.name}))}};const W=(0,c.A)(D,[["render",N],["__scopeId","data-v-2077adc6"]]);var G=W;const H=[{path:"/",name:"Home",component:F},{path:"/:name/:id/reviews",name:"Review",component:G}],K=(0,d.aE)({history:(0,d.LA)(),routes:H});var U=K;(0,r.Ef)(l).use(U).mount("#app")}},t={};function n(r){var o=t[r];if(void 0!==o)return o.exports;var a=t[r]={exports:{}};return e[r].call(a.exports,a,a.exports,n),a.exports}n.m=e,function(){var e=[];n.O=function(t,r,o,a){if(!r){var s=1/0;for(l=0;l<e.length;l++){r=e[l][0],o=e[l][1],a=e[l][2];for(var i=!0,c=0;c<r.length;c++)(!1&a||s>=a)&&Object.keys(n.O).every((function(e){return n.O[e](r[c])}))?r.splice(c--,1):(i=!1,a<s&&(s=a));if(i){e.splice(l--,1);var u=o();void 0!==u&&(t=u)}}return t}a=a||0;for(var l=e.length;l>0&&e[l-1][2]>a;l--)e[l]=e[l-1];e[l]=[r,o,a]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="/"}(),function(){var e={524:0};n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,a,s=r[0],i=r[1],c=r[2],u=0;if(s.some((function(t){return 0!==e[t]}))){for(o in i)n.o(i,o)&&(n.m[o]=i[o]);if(c)var l=c(n)}for(t&&t(r);u<s.length;u++)a=s[u],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(l)},r=self["webpackChunkratemycourses_frontend"]=self["webpackChunkratemycourses_frontend"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=n.O(void 0,[504],(function(){return n(674)}));r=n.O(r)})();
//# sourceMappingURL=app.1d7b6cd8.js.map