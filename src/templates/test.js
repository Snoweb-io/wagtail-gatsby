import React from "react"
import {graphql} from "gatsby"

export default function TestTemplate({data}) {
    const {page} = data.wagtail
    return (
        <div>
            <h1>test</h1>
            {page.body.map((block) => (
                block.value
            ))}
        </div>
    )
}

export const query = graphql`
    query($slug: String) {
        wagtail {
            page(slug: $slug) {
                ... on TestPage {
                    body {
                        ... on RichTextBlock {
                            value
                            blockType
                        }
                    }
                }
            }
        }
    }
`