import React from 'react'
// import ReactDOM from 'react-dom';
import styles from './temp.module.css'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
// import DeleteIcon from '@mui/icons-material/Delete';
// import AlarmIcon from '@mui/icons-material/Alarm';
// import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';

const Temp = () => {
    // const element = React.createElement(
    //     'h1',
    //     {className: 'greeting'},
    //     'Hello, world!'
    // );
    // 렌더링 된 엘리먼트를 업데이트 하려면 새로운 엘리먼트를 생성하고 이를
    // root.render()로 전달해야 함
    // const root = ReactDOM.createRoot(
    //     document.getElementById('root')
    // );
    // function tick() {
    //   const element = (
    //    <div>
    //     <h1>Hello, world!</h1>
    //     <h2>It is {new Date().toLocaleTimeString()}.</h2>
    //    </div>

    //   )
    //   root.render(element);
    // }
    // setInterval(tick, 1000)
    // const element = <h1>Hello, world</h1>
  return (
    <Stack spacing={2} direction="row">
      <Button variant='text'>Text</Button>
      <IconButton aria-label='delete'>
        {/* <DeleteIcon /> */}
      </IconButton>
    
      <div className={styles.Box}> this is temp </div>

    </Stack>
    // <div id='root'></div>
    // <div> hello world </div>
    // element
  )
}

export default Temp