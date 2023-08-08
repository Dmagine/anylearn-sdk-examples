from anylearn.config import init_sdk
from anylearn.interfaces.user import User

# print("测试用户注册")
# init_sdk('http://192.168.10.22:30128', 'wangtuantuan', 'abc123')
# user = User(username="TestZhuCe",password="abc123",email="abc@123.com")
# res = user.save()
# print(f"注册结果为：{res}")

# print("测试用户删除")
# init_sdk('http://192.168.10.22:30128', 'xlearn', '123456')
# user = User(id="USER119ebf5911eb9dcb1a45aa295e24")
# res = user.delete()
# print(f"删除结果为：{res}")

# print("测试修改密码")
# init_sdk('http://192.168.10.22:30128', 'TestZhuCe', 'abc123')
# user = User(id="USER108cbf5911eb9dcb1a45aa295e24")
# res = user.change_password(old_password="abc123",new_password="123456")
# print(f"修改密码结果为：{res}")

print("测试修改用户信息")
init_sdk('http://192.168.10.22:30128', 'TestZhuCe', '123456')
user = User(id="USER108cbf5911eb9dcb1a45aa295e24", email="testedit@126.com")
res = user.save()
print(f"修改用户信息结果为：{res}")

print("测试获取用户详情")
init_sdk('http://192.168.10.22:30128', 'TestZhuCe', '123456')
user = User(id="USER108cbf5911eb9dcb1a45aa295e24")
user.get_detail()
print(f"用户详情结果为：{user}")

print("测试获取用户集合")
init_sdk('http://192.168.10.22:30128', 'TestZhuCe', '123456')
user = User(id="USER108cbf5911eb9dcb1a45aa295e24")
res = user.user_collection(
    ids="USER108cbf5911eb9dcb1a45aa295e24,USERe5e6bc5c11eb96608295a54cd0ac")
print(f"用户集合结果为：{res}")

print("测试获取用户集合")
init_sdk('http://192.168.10.22:30128', 'TestZhuCe', '123456')
res = User.get_list()
print(f"用户集合结果为：{res}")

print("测试用户名查重")
init_sdk('http://192.168.10.22:30128', 'TestZhuCe', '123456')
res = User.user_check(username="TestZhuCe")
print(f"用户名查重结果为：是否重复？{res}")
res = User.user_check(username="TestZhuCe11")
print(f"用户名查重结果为：是否重复？{res}")
