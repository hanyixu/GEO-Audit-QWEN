#!/bin/bash

# GEO Audit QWEN - 卸载脚本
# 适用于 macOS / Linux / Windows (Git Bash)

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_success() {
    echo -e "${GREEN}✅ ${1}${NC}"
}

print_error() {
    echo -e "${RED}❌ ${1}${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  ${1}${NC}"
}

print_info() {
    echo -e "   ${1}"
}

# 标题
echo -e "\n${RED}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${RED}║${NC}  ${YELLOW}GEO Audit QWEN - 卸载程序${NC}                          ${RED}║${NC}"
echo -e "${RED}╚════════════════════════════════════════════════════════╝${NC}\n"

# 确认卸载
echo -e "${YELLOW}⚠️  警告：此操作将删除以下文件：${NC}"
echo -e "   • Qwen Code 技能文件 (~/.qwen/skills/geo-*)"
echo -e "   • Agent 配置文件 (~/.qwen/agents/geo-*.md)"
echo -e "   • 本地项目文件 (~/.geo-audit-qwen/)\n"

read -p "确认卸载？(y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "\n${BLUE}已取消卸载${NC}"
    exit 0
fi

# 删除技能文件
echo -e "\n${BLUE}[1/4]${NC} 删除技能文件..."

for skills_dir in "$HOME/.qwen/skills" "$HOME/.claude/skills"; do
    if [ -d "$skills_dir" ]; then
        count=0
        for skill in "$skills_dir"/geo-*; do
            if [ -e "$skill" ]; then
                rm -rf "$skill"
                count=$((count + 1))
            fi
        done
        if [ $count -gt 0 ]; then
            print_success "已删除 $count 个技能: $skills_dir/geo-*"
        fi
    fi
done

# 删除Agent文件
echo -e "\n${BLUE}[2/4]${NC} 删除 Agent 文件..."

for agents_dir in "$HOME/.qwen/agents" "$HOME/.claude/agents"; do
    if [ -d "$agents_dir" ]; then
        count=0
        for agent in "$agents_dir"/geo-*.md; do
            if [ -e "$agent" ]; then
                rm -f "$agent"
                count=$((count + 1))
            fi
        done
        if [ $count -gt 0 ]; then
            print_success "已删除 $count 个 Agent 文件: $agents_dir/geo-*.md"
        fi
    fi
done

# 删除本地项目文件
echo -e "\n${BLUE}[3/4]${NC} 删除本地项目文件..."

if [ -d "$HOME/.geo-audit-qwen" ]; then
    rm -rf "$HOME/.geo-audit-qwen"
    print_success "已删除项目文件: $HOME/.geo-audit-qwen"
else
    print_info "未找到项目文件（可能未安装）"
fi

# 提示保留数据
echo -e "\n${BLUE}[4/4]${NC} 保留数据..."
print_info "以下数据未被删除（如需删除请手动操作）："
print_info "  • CRM 数据: ~/.geo-prospects/"
print_info "  • Python 依赖包（可通过 pip uninstall 删除）"

# 完成
echo -e "\n${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║${NC}              ${YELLOW}🗑️  卸载完成！${NC}                            ${GREEN}║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${BLUE}如需重新安装，请运行：${NC}"
echo -e "   ${YELLOW}curl -fsSL https://raw.githubusercontent.com/hanyixu/GEO-Audit-QWEN/main/install.sh | bash${NC}\n"

exit 0
