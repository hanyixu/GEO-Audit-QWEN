class GeoAudit < Formula
  desc "GEO Audit Tool - 为中文AI搜索引擎优化网站"
  homepage "https://github.com/hanyixu/GEO-Audit-QWEN"
  url "https://github.com/hanyixu/GEO-Audit-QWEN/archive/refs/heads/main.tar.gz"
  version "1.0.0"
  sha256 "PLACEHOLDER_SHA256"
  license "MIT"

  depends_on "python@3.8"
  depends_on "git"

  def install
    # 安装到 Cellar
    libexec.install Dir["*"]

    # 创建可执行文件
    (bin/"geo-audit").write <<~EOS
      #!/bin/bash
      exec "#{libexec}/install.sh" "$@"
    EOS
  end

  def caveats
    <<~EOS
      GEO Audit 安装完成！

      使用方法：
        1. 打开 Qwen Code (输入 qwen)
        2. 运行审计: /geo audit https://你的网站.com

      文档: https://github.com/hanyixu/GEO-Audit-QWEN#readme
    EOS
  end

  test do
    system "#{bin}/geo-audit", "--help"
  end
end
