select  
	invtypes.marketGroupID as marketID, 
	me_industry.typeID as bpID, 
	invtypes.typeName as bpName 
from me_industry
left JOIN invtypes on me_industry.typeID = invtypes.typeID
where invtypes.marketGroupID is not null
ORDER BY me_industry.typeID
;
