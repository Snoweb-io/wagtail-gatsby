import { prepareOptions } from "gatsby/dist/utils/babel-loader-helpers";

exports.prepareOptions = (babel, options = {}, resolve = require.resolve) => {
  return prepareOptions(babel, options, resolve);
};
