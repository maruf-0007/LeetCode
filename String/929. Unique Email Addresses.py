class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s=set()
        for i in emails:
            local,domain=i.split("@")
            if "+" in local:
                local=local.split("+")[0].replace(".","")
            else:
                local=local.replace(".","")
            new=local+"@"+domain
            s.add(new)
        return len(s)