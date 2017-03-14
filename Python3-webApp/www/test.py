#!/usr/bin/env python3
# condig=utf-8

import orm,asyncio
from models import User, Blog, Comment


import orm
from models import User, Blog, Comment

async def destory_pool():
	#global __pool
	if orm.__pool is not None :
		orm.__pool.close()
		await orm.__pool.wait_closed()

async def test(loop):
	await orm.create_pool(loop=loop,user='www-data', password='www-data', database='awesome')

	u = User(name='Test2', email='test2@example.com', passwd='1234567899', image='about:blank')

	await u.save()

	# await User(id='0014894924243715d78e29eaa31416da3fe46584614f8cd000').remove()
	# r = await User.findAll() 
	await destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()