# 468. Validate IP Address
# Medium
# Companies
# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
#
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
#
#
#
# Example 1:
#
# Input: queryIP = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
# Example 2:
#
# Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".
# Example 3:
#
# Input: queryIP = "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.
#
#
# Constraints:
#
# queryIP consists only of English letters, digits and the characters '.' and ':'.


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """
        - 일단 깡으로 풀자. 그리고 정규식 쓰자.
        - 정규 표현식을 쓴다. (정할 정, 법칙 규, 겉 표, 나타날 현)
            - 문자열 집합을 나타내기 위한 기호 표현 규칙
            - regular expression
            - 알고리즘 연습은 아닌 느낌 -> 정규식 연습에 가깝다.
        - 깡으로 푼다.
            - 3개 중 하나이다.
                - isIP4v()
                    - 아래 구조인가?
                        - x0.x1.x2x.x3
                        - . 이 3개 있는가?
                        - . 으로 분리한 아이템이 4개인가?
                    - reading 제로가 없는가?
                        - 2글자 이상일 떄 앞에 0이 있으면 에러
                    - 아이템이 전부 숫자인가
                    - 숫자로 변환
                    - 0 <= x <= 255 안 인가?
                - isIP6v()
                    - 아래 구조인가?
                    - x0:x1:x2:x3:x4:x5:x6:x7
                    - 전부 로우케이스로 변경
                    - 최대 4자리인지
                    - 모든 엘리먼트가 한 개 이상인지 확인
                    - 모든 알파뱃이 0-9,a-f 인지 확인
                        - a 10
                        - b 11
                        - c 12
                        - d 13
                        - e 14
                        - f 15
                - Neither
        """

        if self.valid_Ip4(queryIP):
            return "IPv4"
        elif self.valid_Ip6(queryIP):
            return "IPv6"

        return "Neither"

    def valid_Ip6(self, query_ip: str) -> bool:
        query_ip = query_ip.lower()
        arr = query_ip.split(":")
        if len(arr) != 8:
            return False

        for ele in arr:
            if len(ele) > 4 or len(ele) == 0:
                return False
            for char in ele:
                if char not in [
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                ]:
                    return False

        return True

    def valid_Ip4(self, query_ip: str) -> bool:
        arr = query_ip.split(".")
        if len(arr) != 4:
            return False

        for ele in arr:
            if len(ele) >= 2 and ele[0] == "0":  # verify reading zero
                return False

            if not ele.isnumeric():
                return False

            if not (0 <= int(ele) <= 255):
                return False

        return True


def test_valid_ipv6():
    s = Solution()
    t1 = dict(input="2001:0db8:85a3:0:0:8A2E:0370:7334", output=True)
    # t2 = dict(input="172.16.254.01", output=False)
    # t3 = dict(input="256.16.254.1", output=False)
    # t4 = dict(input="-1.16.254.1", output=False)
    # t5 = dict(input="a.16.254.1", output=False)
    # t6 = dict(input="16.254.1", output=False)
    #
    # ts = [t1, t2, t3, t4, t5, t6]

    ts = [t1]
    for t in ts:
        assert s.valid_Ip6(t["input"]) == t["output"]


def test_valid_ipv4():
    s = Solution()
    t1 = dict(input="172.16.254.1", output=True)
    t2 = dict(input="172.16.254.01", output=False)
    t3 = dict(input="256.16.254.1", output=False)
    t4 = dict(input="-1.16.254.1", output=False)
    t5 = dict(input="a.16.254.1", output=False)
    t6 = dict(input="16.254.1", output=False)

    ts = [t1, t2, t3, t4, t5, t6]
    for t in ts:
        assert s.valid_Ip4(t["input"]) == t["output"]


def test_valid_ip():
    s = Solution()
    t1 = dict(input="172.16.254.1", output="IPv4")
    t2 = dict(input="2001:0db8:85a3:0:0:8A2E:0370:7334", output="IPv6")
    t3 = dict(input="", output="Neither")

    ts = [t1]
    for t in ts:
        assert s.validIPAddress(t["input"]) == t["output"]
