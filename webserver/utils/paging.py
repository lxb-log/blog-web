

def pager_limit(request, qs, *orders):
    """
	传入偏移值offset, 页数量限制limit
	"""
    total = qs.count()
    limit = request.GET.get("limit")
    offset = request.GET.get("offset")
    limit = int(limit) if limit else 10
    offset = int(offset) if offset else 0
    if orders:
        qs = qs.order_by(*orders)[offset:offset + limit]
    else:
        qs = qs[offset:offset + limit]
    meta = {'limit': limit, 'offset': offset, 'total': total}

    return qs, meta


def pager_page(request, qs, PageSize, *orders):
    """
	传入页容量PageSize, 接收页码
	"""
    amount = qs.count()  # 计算查询集中对象的数量
    # 总页数
    page_count = amount // PageSize + 1 if amount % PageSize != 0 else amount // PageSize
    # 接收页码
    page = request.GET.get('page')
    # 如果pege存在
    if page:
        # 如果page是由纯数字组成 和 page小于等于总页码, 否则page=1
        page = int(page) if str(page).isdigit() and int(page) <= page_count else 1
        #
        if orders:
            # 如果传入的有orders值, 就先排序, 再使用切片取值
            qs = qs.order_by(*orders)[(page-1)*PageSize : page*PageSize]

        else:
            qs = qs[(page-1)*PageSize : page*PageSize]
    # 结束后返回指定页的查询集数据,页码, 以及总页码
    return qs, page, page_count