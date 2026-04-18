# Contributing to Sloth-Sales-Eido

Thank you for your interest in improving the B2B Sales Intelligent Assistant!

## Project Structure

```
Sloth-Sales-Eido/
├── SKILL.md              # Main skill definition (v4.1 Complete Edition)
├── README.md             # Chinese documentation
├── README_EN.md          # English documentation
├── reference.md          # Data model & health scoring rules
├── examples.md           # Interaction examples
├── User_Guide.md         # English user guide
├── 用户使用手册.md         # Chinese user guide
├── scripts/
│   └── init_db.py        # SQLite database initialization
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
├── v1.0-P0-核心CRM/       # Version 1.0 archive
├── v2.0-P1-智能增强/      # Version 2.0 archive
├── v3.0-P2-分析竞争/      # Version 3.0 archive
└── v4.0-P3-完整版/        # Version 4.0 archive
```

## Version Directories

Each `v*` directory contains a complete, standalone snapshot of the skill at that development stage. These are preserved for reference and should not be modified.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest features
- Include your QoderWork version and steps to reproduce

### Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes to the root-level files (not version directories)
4. Test with QoderWork to verify the skill works correctly
5. Submit a Pull Request with a clear description

### SKILL.md Guidelines

- Follow the existing YAML frontmatter format (`name`, `description`)
- Keep the description concise but comprehensive
- Maintain backward compatibility with existing database schemas
- Document any new database tables or columns in `reference.md`

### Documentation Standards

- Maintain both Chinese (`README.md`) and English (`README_EN.md`) documentation
- Update `CHANGELOG.md` when adding features
- Add interaction examples in `examples.md` for new capabilities

### Database Changes

- All schema changes must be backward-compatible
- Update `scripts/init_db.py` for new tables or columns
- Update `reference.md` with field definitions
- Use JSON fields for flexible data storage where appropriate

## Code of Conduct

Be respectful, constructive, and collaborative. We welcome contributors of all experience levels.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
