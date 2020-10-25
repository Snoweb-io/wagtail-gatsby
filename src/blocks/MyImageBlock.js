import React from 'react';

const MyImageBlock = (props) => {
    const {image} = props;
    return (
        <img src={image.url} alt={image.title}/>
    )
};

export default MyImageBlock;
