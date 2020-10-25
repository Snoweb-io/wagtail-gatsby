import React from 'react';

const MyTextBlock = (props) => {
    const {text} = props;
    return (
        <div
            dangerouslySetInnerHTML={{
                __html: text
            }}
        />
    )
};

export default MyTextBlock;
