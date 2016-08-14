"use strict"

import importDir from 'import-dir'
import compose from 'koa-compose'
import Router from 'koa-router'

const routerConfig = [
  { folder: 'abuse', prefix: '/api' },
  { folder: 'post', prefix: '/api' },
  { folder: 'admin', prefix: '/moderate' },
]

export default function api() {
  const composed_route = routerConfig.reduce((prev, curr) => {
    const routes = importDir('./' + curr.folder)
    const router = new Router({ prefix: curr.prefix })

    Object.keys(routes).map(name => routes[name](router))
    return [router.routes(), ...prev]
  }, [])

  return compose(composed_route)
}
