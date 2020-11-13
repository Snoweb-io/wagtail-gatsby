import {graphql} from "gatsby";

export const PageFragment = graphql`
    fragment PageFragment on wagtail {
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
`
