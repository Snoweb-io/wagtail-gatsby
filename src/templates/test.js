import React from "react"
import {graphql} from "gatsby"
import * as blocks from '../blocks';

export default function TestTemplate({data}) {
    const {page} = data.wagtail;
    console.log(page);
    return (
        <div>
            {page.body.map((block) => {
                const BlockComponent = blocks[block.blockType];
                console.log(blocks[block.blockType]);
                return (
                    <BlockComponent {...block} />
                )
            })}
        </div>
    )
}

export const query = graphql`
    query($slug: String) {
        wagtail {
            page(slug: $slug) {
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
`