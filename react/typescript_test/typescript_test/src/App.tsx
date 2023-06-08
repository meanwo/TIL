import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './App.css';
import Home from './components/Home'
import NotFound from './components/NotFound'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
    errorElement: <NotFound />,
    children: [
      {index :true, element: <Home/>},
      {path: '/test', element: <Test/>}
      
    ]
  }
]);
export default function App() {
  return (
    <div>
      <RouterProvider router={router}/>
    </div>
  );
};