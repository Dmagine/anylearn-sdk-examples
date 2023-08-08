# Anylearn-SDK 示例（Jupyter Notebook形式）

### SDK内部发布阶段

目前SDK仍在开发调试中，暂未发布到PyPI，因此需以pip从GitHub（本库）安装`anylearn-sdk`，以正常运行当前目录下的jupyter notebook示例。安装命令如下：
```shell
pip install -U git+https://<github_api_token>@github.com/Dmagine/Anylearn-sdk.git@<anylearn_sdk_version>
```
其中需替换`<github_token>`部分为真实的GitHub API access token（参见[](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)），并替换`<anylearn_sdk_version>`为希望使用的SDK版本，例如：`0.11-alpha9`。

### SDK开发者（build from source）
对于开发者，可以通过本地源文件构建并安装。

于源码根目录下进行构建：
```shell
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements_dev.txt
python setup.py bdist_wheel
deactivate
```
生成`dist`目录，其中包含构建好的wheel包`anylearn-<version>-py3-none-any.whl`，其中`<version>`为当前版本号。

于本目录（`<path-to-anylearn-sdk>/examples/jupyter`）下进行安装：
```shell
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install ../../dist/anylearn-<version>-py3-none-any.whl
```
