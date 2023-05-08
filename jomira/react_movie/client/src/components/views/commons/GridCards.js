import React from 'react'
import { Col } from 'antd';

function GridCards(props) {
  if (props.randingPage){
    return (
      <Col lg={4} md={8} xs={12}>
        <div style={{ position: 'relative' }}>
          <a href={`/movie/${props.movieId}`}>
            <img style={{ width:'100%', height:'auto' }} src={props.image} alt={props.movieName} />
          </a>
        </div>
      </Col>
    )
  }else {
    return (
      <Col lg={4} md={8} xs={12}>
        <div style={{ position: 'relative' }}>
            <img style={{ width:'100%', height:'auto' }} src={props.image} alt={props.characterName} />
        </div>
      </Col>
    )
  }
}

export default GridCards