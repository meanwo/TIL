import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const Topbar = () => {
    const [topName, setTopName] = useState('default')
	const navigate = useNavigate();

    // 현재 url 정보를 가져오는 useLocation
    const location = useLocation()


    return (
        <div>
            this is top-bar   
        </div>
    );
};


export default Topbar;