class Solution:
    def numUniqueEmails(self, emails) -> int:
        res = set()
        for i in emails:
            local, domain = i.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))

            res.add('@'.join([local, domain]))

        return len(res)