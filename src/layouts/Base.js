import React from 'react';
import { Helmet } from 'react-helmet';
import { createGlobalStyle } from 'styled-components';

import { Card } from '../components';

const GlobalStyle = createGlobalStyle`
  h1, h2, h3, h4, h5, h6, p {
    font-family: 'Lato', sans-serif;
  }
`;

const Base = (props) => {
  const { page, children } = props;
  return (
    <>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{page.seoTitle}</title>
        <link rel="canonical" href="" />
        <meta name="description" content={page.seoDescription} />
        <meta name="author" content="" />
        <meta name="content-language" content="" />
        <meta property="og:type" content="website" />
        <meta property="og:title" content="" />
        <meta property="og:description" content="" />
        <meta property="og:image" content="" />
        <meta property="og:image:width" content="" />
        <meta property="og:image:height" content="" />
        <meta property="og:url" content="" />
        <meta name="twitter:title" content="" />
        <meta name="twitter:description" content="" />
        <meta name="twitter:image" content="" />
        <meta name="twitter:card" content="" />
        <meta name="theme-color" content="" />
      </Helmet>
      <GlobalStyle />
      <Card>{children}</Card>
    </>
  );
};

export default Base;
