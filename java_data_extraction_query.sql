SELECT p.Id, p.PostTypeId, p.ParentId, p.Score, p.Body, p.ViewCount, p.FavoriteCount, p.Title, p.Tags, a.body
FROM Posts p
JOIN Posts a on p.AcceptedAnswerId = a.id
WHERE p.tags like ('%java%')
AND p.tags Not like('%javascript%')
AND p.AcceptedAnswerId IS NOT NULL
AND p.ClosedDate IS NULL
AND p.DeletionDate IS NULL
AND p.Score > 7
AND (
	(lower(p.title) like('how %') or lower(p.title) like('is it%') or lower(p.title) like('what to%') or lower(p.title) like('why %'))
)
