// Models
import { IDModel } from '../../model/post'
import { TopModel } from '../../model/top'

export default (router) => {
  router

    .get('/post/top', // All year top posts
         top_handler)
}

async function top_handler(ctx, next) {
  let postKey = []
  const postID = await IDModel.find().exec()

  await Promise.all(postID.map((value) => {
    postKey.push(value.postKey)
  }))

  const limitPageResult = ctx.query['count'] ? ctx.query['count'] : 20

  const top = await TopModel.find({
    _id: { $in: postKey },
    'status.delivered': true
  })
  .sort('-totalScore')
  .limit(limitPageResult)
  .select('postid')
  .exec()

  ctx.body = { success: true, results: top }
}
