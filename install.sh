#!/bin/bash

# GEO Audit QWEN - 一键安装脚本
# 适用于 macOS / Linux

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_step() {
    echo -e "\n${BLUE}[${1}]${NC} ${2}"
}

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
echo -e "\n${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║${NC}  ${YELLOW}GEO Audit QWEN - 安装程序${NC}                          ${GREEN}║${NC}"
echo -e "${GREEN}║${NC}  为中文AI搜索引擎优化你的网站                    ${GREEN}║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}\n"

# [1/6] 检查依赖
print_step "1/6" "检查系统依赖..."

# 检查 Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version | awk '{print $3}')
    print_success "Git 已安装: ${GIT_VERSION}"
else
    print_error "未检测到 Git，请先安装 Git"
    print_info "macOS: brew install git"
    print_info "Ubuntu/Debian: sudo apt-get install git"
    exit 1
fi

# 检查 Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    print_success "Python3 已安装: ${PYTHON_VERSION}"
else
    print_warning "未检测到 Python3，部分功能可能不可用"
    print_info "你可以继续使用基础功能，或安装 Python 3.8+"
fi

# 检查 Qwen Code
if command -v qwen &> /dev/null; then
    print_success "Qwen Code 已安装"
    QWEN_SKILLS_DIR="$HOME/.qwen/skills"
elif command -v claude &> /dev/null; then
    print_success "Claude Code 已安装（兼容模式）"
    QWEN_SKILLS_DIR="$HOME/.claude/skills"
else
    print_warning "未检测到 Qwen Code 或 Claude Code"
    print_info "请安装 Qwen Code 后再使用 GEO 审计功能"
    print_info "安装指南: https://github.com/anthropics/claude-code"
    # 询问是否继续
    echo ""
    read -p "是否继续安装基础文件？(y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
    QWEN_SKILLS_DIR="$HOME/.qwen/skills"
fi

# [2/6] 创建目录
print_step "2/6" "创建安装目录..."

mkdir -p "$QWEN_SKILLS_DIR"
print_success "技能目录已创建: $QWEN_SKILLS_DIR"

# [3/6] 克隆仓库
print_step "3/6" "下载项目文件..."

INSTALL_DIR="$HOME/.geo-audit-qwen"

if [ -d "$INSTALL_DIR" ]; then
    print_warning "检测到已安装的项目，正在更新..."
    cd "$INSTALL_DIR"
    if git pull origin main &> /dev/null; then
        print_success "项目已更新到最新版本"
    else
        print_warning "Git pull 失败，将重新克隆"
        cd ..
        rm -rf "$INSTALL_DIR"
        if git clone https://github.com/hanyixu/GEO-Audit-QWEN.git "$INSTALL_DIR"; then
            print_success "项目下载完成"
        else
            print_error "克隆仓库失败"
            exit 1
        fi
    fi
else
    if git clone https://github.com/hanyixu/GEO-Audit-QWEN.git "$INSTALL_DIR"; then
        print_success "项目下载完成"
    else
        print_error "克隆仓库失败"
        exit 1
    fi
fi

cd "$INSTALL_DIR"

# [4/6] 安装Python依赖
print_step "4/6" "安装 Python 依赖..."

if [ -f "requirements.txt" ] && command -v python3 &> /dev/null; then
    print_info "使用清华镜像源加速下载..."
    if python3 -m pip install -r requirements.txt \
        --index-url https://pypi.tuna.tsinghua.edu.cn/simple \
        --user; then
        print_success "Python 依赖安装完成"
    else
        print_warning "Python 依赖安装失败，可以稍后手动安装"
        print_info "手动安装: pip3 install -r requirements.txt"
    fi
else
    if [ ! -f "requirements.txt" ]; then
        print_info "未找到 requirements.txt，跳过依赖安装"
    fi
fi

# [5/6] 安装技能文件
print_step "5/6" "安装 GEO 技能到 Qwen Code..."

SKILLS_INSTALLED=0

# 安装 14 个子技能
for skill_dir in skills/geo-*/; do
    if [ -d "$skill_dir" ]; then
        skill_name=$(basename "$skill_dir")
        target_dir="$QWEN_SKILLS_DIR/$skill_name"
        
        mkdir -p "$target_dir"
        if [ -f "$skill_dir/SKILL.md" ]; then
            cp "$skill_dir/SKILL.md" "$target_dir/SKILL.md"
            SKILLS_INSTALLED=$((SKILLS_INSTALLED + 1))
        fi
    fi
done

# 安装 Agent 文件
if [ -d "agents" ]; then
    mkdir -p "$HOME/.qwen/agents" 2>/dev/null || mkdir -p "$HOME/.claude/agents" 2>/dev/null || true
    
    AGENTS_DIR="$HOME/.qwen/agents"
    [ -d "$AGENTS_DIR" ] || AGENTS_DIR="$HOME/.claude/agents"
    
    for agent_file in agents/*.md; do
        if [ -f "$agent_file" ]; then
            cp "$agent_file" "$AGENTS_DIR/"
        fi
    done
fi

print_success "已安装 ${SKILLS_INSTALLED} 个技能"

# [6/6] 验证安装
print_step "6/6" "验证安装结果..."

INSTALL_SUCCESS=true

# 检查关键文件
if [ -d "$QWEN_SKILLS_DIR/geo-audit" ]; then
    print_success "主审计技能已安装"
else
    print_error "主审计技能未找到"
    INSTALL_SUCCESS=false
fi

if [ -d "$QWEN_SKILLS_DIR/geo-citability" ]; then
    print_success "引用度评分技能已安装"
else
    print_warning "引用度评分技能未找到（可选）"
fi

# 完成
echo -e "\n${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║${NC}              ${YELLOW}🎉 安装完成！${NC}                            ${GREEN}║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}\n"

echo -e "${BLUE}📁 安装位置:${NC}"
echo -e "   项目文件: ${INSTALL_DIR}"
echo -e "   Qwen 技能: ${QWEN_SKILLS_DIR}/geo-*\n"

echo -e "${BLUE}🚀 开始使用:${NC}"
echo -e "   1. 打开 Qwen Code (输入 ${YELLOW}qwen${NC})"
echo -e "   2. 运行审计: ${YELLOW}/geo audit https://你的网站.com${NC}\n"

echo -e "${BLUE}📖 查看文档:${NC}"
echo -e "   https://github.com/hanyixu/GEO-Audit-QWEN#readme\n"

if [ "$INSTALL_SUCCESS" = false ]; then
    print_warning "部分文件安装失败，请检查上述错误信息"
    exit 1
fi

exit 0
