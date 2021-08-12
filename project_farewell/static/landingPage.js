new Swiper(".movie .swiper-container", {
  //autoplay: true,
  loop: true,
  spaceBetween: 20, //슬라이드 사이 여백
  slidesPerView: 3, //한번에 다섯개의 슬라이드 보이게

  navigation: {
    //슬라이드 좌우로 이동하는 버튼에 대한 명시
    prevEl: ".movie .swiper-prev", //왼쪽 버튼 요소 선택자
    nextEl: ".movie .swiper-next", //오른쪽 버튼 요소 선택자
  },
});
