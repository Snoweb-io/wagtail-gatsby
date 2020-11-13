import React from 'react';
import { graphql } from 'gatsby';

import * as blocks from '../blocks';
import { Base } from '../layouts';

const TestPage = ({ data }) => {
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
        ... on wagtail_TestPage {
          body {
            ... on wagtail_MyTextBlock {
              blockType
              text
            }
            ... on wagtail_MyImageBlock {
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

export default TestPage;
