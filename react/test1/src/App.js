// lint 끄는 기능
/* eslint-disable */


import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let post = '강남 우동 맛집';
  // 자료를 잠깐 저장할 땐 state를 써도 됨
  // a: state에 보관했던 자료
  // b: state 변경 도와주는 함수

  // state는 변수가 변경되면 state 쓰던 html이 자동으로 재 렌더링됨
  let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동 맛집', '파이썬 독학']);
  let [따봉, 따봉변경] = useState(0);

  function 함수() {
    따봉변경(따봉+1);
  }

  return (
    // JSX문법1. class를 className으로 선언
    // JSX문법2. 데이터 바인딩은 중괄호{}
    // JSX문법3. style 넣을 땐 style = {}
    <div className="App">
      <div className="black-nav">
        <h4 style = { {color : 'red', fontSize : '16px'} } id={post}>ReactBlog</h4>
      </div>

      <button onClick={()=>{
        let copy = [...글제목];
        copy = copy.sort()
        글제목변경(copy)
      }
      }> 가나다순정렬 </button>



      <button onClick={()=>{
        // array/object 다룰 때 원본은 보존하는 게 좋음
        
        // let copy = 글제목;
        // copy[0] = '여자코트 추천';
        // console.log(copy == 글제목);  // 변수1 & 변수2 화살표가 같으면 변수1 ==변수2 비교해도 true 나옴
        
        // ...는 글제목에 있던 괄호를 벗기고 내용만 가져욤.
        // 이후 다시 괄호를 씌우면 새로운 state를 선언하는 방식임.
        let copy = [... 글제목];
        copy[0] = '여자코트 추천';
        글제목변경(copy)
      }}>글 수정</button>

      <div className='list'>
        <h4>{ 글제목[0] } <span onClick={ 함수 }>👍</span> { 따봉 } </h4>
        <p>2월 17일 발행</p>
      </div>
      {/* <h4>{ post }</h4> */}
      <div className='list'>
        <h4>{ 글제목[1] }</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className='list'>
        <h4>{ 글제목[2] }</h4>
        <p>2월 17일 발행</p>
      </div>
      

      {/* <Modal></Modal> */}
      <Modal/>


    </div>
  );
}

// 컴포넌트 함수를 const 선언해서 사용할 수도 있음
// const Modal = () => {
//   return (

//   )
// }

function Modal() {
  return (
    <>
      <div className='modal'>
        <h4>제목</h4>
        <p>날짜</p>
        <p>상세내용</p>
      </div>
    </>
  )
}
export default App;
