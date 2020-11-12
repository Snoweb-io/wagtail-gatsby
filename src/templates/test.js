import React from 'react';
import { graphql } from 'gatsby';

import * as blocks from '../blocks';
import { Base } from '../layouts';

export default ({ data }) => {
  const { page } = data.wagtail;
  console.log(data);
  return (
    <Base page={page}>
      {page.body.map((block, key) => {
        const BlockComponent = blocks[block.blockType];
        return <BlockComponent key={key} {...block} />;
      })}
    </Base>
  );
};

export const query = graphql`
  query($slug: String) {
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
`;
