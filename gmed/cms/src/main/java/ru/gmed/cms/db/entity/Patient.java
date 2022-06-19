package ru.gmed.cms.db.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.Generated;
import org.hibernate.annotations.GenerationTime;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.data.annotation.CreatedDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Version;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@NoArgsConstructor
@Builder
@Getter
@Setter
public class Patient {
    @Id
    @Column(name = "id", nullable = false)
    @Generated(GenerationTime.ALWAYS)
    private UUID id;

    private String fio;
    @CreatedDate
    private LocalDateTime createDate;
    @UpdateTimestamp
    private LocalDateTime updateDate;
    @Version
    private Integer version;
    private LocalDateTime deleteDate;
    private boolean deleted;
}
