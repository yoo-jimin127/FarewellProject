/* 썸네일 미리보기 */
const inputThumbnailEl = document.querySelector("#input__thumbnail");
function readImage(input) {
  // 인풋 태그에 파일이 있는 경우
  if (input.files && input.files[0]) {
    // 이미지 파일인지 검사 (생략)
    // FileReader 인스턴스 생성
    const reader = new FileReader();
    // 이미지가 로드가 된 경우
    reader.onload = (e) => {
      const thumbnailWrapperEl = document.querySelector(".thumbnail__wrapper");
      //기존 프리뷰 지우기
      const beforePreviewImage = document.querySelector(
        ".thumbnail__wrapper .thumbnail"
      );
      if (beforePreviewImage) {
        beforePreviewImage.remove();
      }
      //새로운 프리뷰 보여주기
      const previewImage = document.createElement("img");
      previewImage.src = e.target.result;
      previewImage.className = "thumbnail";
      thumbnailWrapperEl.appendChild(previewImage);
    };
    // reader가 이미지 읽도록 하기
    reader.readAsDataURL(input.files[0]);
  }
}
//인풋태그에 change 이벤트 부여
inputThumbnailEl.addEventListener("change", (e) => {
  readImage(e.target);
});

/* 유튜브 링크 입력하면 미리보기 */
const inputYoutubeIdEl = document.querySelector("#input__youtubeId");
inputYoutubeIdEl.addEventListener("change", (e) => {
  readYoutube(e.target.value);
});

function readYoutube(youtubeId) {
  const youtubePreviewElWrapper = document.querySelector(".movie__preview");
  //기존 프리뷰 지우기
  const beforeYoutubePreviewEl = document.querySelector(
    ".movie__preview iframe"
  );
  if (beforeYoutubePreviewEl) {
    beforeYoutubePreviewEl.remove();
  }

  const youtubePreviewEl = document.createElement("iframe");
  youtubePreviewEl.src = `https://www.youtube.com/embed/${youtubeId}`;
  youtubePreviewEl.title = "YouTube video player";
  youtubePreviewEl.frameborder = "0";
  youtubePreviewEl.allow =
    "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
  youtubePreviewEl.setAttribute("allowfullscreen", true);
  youtubePreviewElWrapper.appendChild(youtubePreviewEl);
}

/* textarea 입력할 때 자동으로 늘어나게 */
const moviePostFormTextareaEl = document.querySelector(
  ".moviePostForm__main textarea"
);

function resizeMoviePostFormTextarea() {
  moviePostFormTextareaEl.style.height = "1px";
  moviePostFormTextareaEl.style.height = `${
    15 + moviePostFormTextareaEl.scrollHeight
  }px`;
}

moviePostFormTextareaEl.addEventListener(
  "keydown",
  resizeMoviePostFormTextarea
);
moviePostFormTextareaEl.addEventListener("keyup", resizeMoviePostFormTextarea);
