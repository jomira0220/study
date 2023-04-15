import React, { useEffect, useState } from 'react'
import { FaCode } from "react-icons/fa";
import { API_KEY, API_URL, IMAGE_BASE_URL } from '../../Config';
import MainImage from './Sections/MainImage';
import axios from 'axios';
import GridCards from '../commons/GridCards';
import { Row } from 'antd';

function LandingPage() {
    
    const [Movies,setMovies] = useState([])
    const [MainMovieImage,setMainMovieImage] = useState(null)
    
    useEffect(()=>{
        const endPoint = `${API_URL}movie/popular?api_key=${API_KEY}&language=en&page=1`
        
        fetch(endPoint)
        .then(response => response.json())
        .then(response => { 
            console.log(response)
            setMovies([response.results]) 
            setMainMovieImage(response.results[0])
        })
        
        
        
    },[])
    
    
    return (
        <div style={{ width: '100%', margin: '0'}}>
            
            {/* Main Image */}
            {MainMovieImage &&
                <MainImage 
                title={MainMovieImage.original_title}
                text={MainMovieImage.overview}
                image={`${IMAGE_BASE_URL}w1280${MainMovieImage.backdrop_path}`}/>
            }
            
            <div style={{ width: '85%', margin: '1rem auto'}}>
                <h2>Movie by latest</h2>
                <hr/>
                { /* Movie Grid Cards */ }
                <Row>
                    {Movies && Movies.map((movie, index) => (
                        <React.Fragment key={index}>
                            <GridCards 
                                image={movie.poster_path ? `${IMAGE_BASE_URL}w500${movie.poster_path}` : null}
                                movieId={movie.id}
                                movieName={movie.original_title} 
                            />  
                        </React.Fragment>
                    ))}
                </Row>
            
            </div>
            
            <div style={{ display: 'flex', justifyContent: 'center'}}>
                <button>Load more</button>
            </div>
            
        </div>
    )
}

export default LandingPage
