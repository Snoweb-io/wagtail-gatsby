import React from 'react';
import { graphql } from 'gatsby';

import * as blocks from '../blocks';
import { Base } from '../layouts';

export default function TestTemplate({ data }) {
  const { page } = data.wagtail;
  return (
    <Base page={page}>
      {page.body.map((block, key) => {
        const BlockComponent = blocks[block.blockType];
        return <BlockComponent key={key} {...block} />;
      })}
    </Base>
  );
}

export const query = graphql`
  query {
    wagtail {
      page(slug: "perfect") {
        seoTitle
        seoDescription
        lastPublishedAt
        ... on TestPage {
          body {
            ... on MyTextBlock {
              blockType
              text
            }
            ... on MyImageBlock {
              blockType
              image {
                url
                title
              }
            }
          }
        }
      }
    }
  }
`;

/*
export const query = graphql`
  query Test($slug: String) {
    wagtail {
      page(slug: $slug) {
        seoTitle
        seoDescription
        lastPublishedAt
        ... on TestPage {
          body {
            ... on MyTextBlock {
              blockType
              text
            }
            ... on MyImageBlock {
              blockType
              image {
                url
                title
              }
            }
          }
        }
      }
    }
  }
`;*/
