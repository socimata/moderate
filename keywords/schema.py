from typing import Literal, TypedDict


class KeywordBase(TypedDict):
    keyword: str


class A1(KeywordBase):
    policy: Literal["A.1 包含违反社会主义核心价值观的内容"]
    type: Literal[
        "传播虚假有害信息",
        "其他法律、行政法规禁止的内容",
        "危害国家安全和利益、损害国家形象",
        "宣扬恐怖主义、极端主义",
        "宣扬暴力、淫秽色情",
        "宣扬民族仇恨",
        "煽动分裂国家、破坏国家统一和社会稳定",
        "煽动颠覆国家政权、推翻社会主义制度",
    ]


class A2(KeywordBase):
    policy: Literal["A.2 包含歧视性内容"]
    type: Literal[
        "信仰歧视内容",
        "健康歧视",
        "其他方面歧视",
        "国别歧视",
        "地域歧视",
        "年龄歧视",
        "性别歧视",
        "民族歧视内容",
        "职业歧视",
    ]


class A3(KeywordBase):
    policy: Literal["A.3 商业违法违规"]
    type: Literal[
        "侵犯他人知识产权",
        "其他商业违法违规行为",
        "利用算法、数据、平台等优势，实施垄断和不正当竞争行为",  # noqa: RUF001
        "泄露他人商业秘密",
        "违反商业道德",
    ]


class A4(KeywordBase):
    policy: Literal["A.4 侵犯他人合法权益"]
    type: Literal[
        "侵害他人个人信息权益；",  # noqa: RUF001
        "侵害他人名誉权",
        "侵害他人肖像权",
        "侵害他人荣誉权",
        "侵害他人隐私权",
        "侵犯他人其他合法权益",
        "危害他人身心健康",
    ]


class A5(KeywordBase):
    policy: Literal["A.5 无法满足特定服务类型的安全需求"]
    type: Literal[
        "内容不准确，严重不符合科学常识或主流认知",  # noqa: RUF001
        "内容不可靠，虽然不包含严重错误的内容，但无法对使用者形成帮助",  # noqa: RUF001
    ]


type Keyword = A1 | A2 | A3 | A4 | A5
