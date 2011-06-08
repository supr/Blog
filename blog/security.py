def groupfinder(uid, request):
    cur = request.db.Groups.find({"username":uid}).limit(1)
    if cur.count() > 0:
        return cur[0].get('group',[])
    return []
